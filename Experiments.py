from ast import arg
import torch
import argparse

# add the arguments
parser = argparse.ArgumentParser(description='PyTorch Brick_kilns')
parser.add_argument('--gpu', type=int, choices=[1,2,3], help='GPU to use')
parser.add_argument('--mode', type=str, choices=["fit","predict","fit-predict","ssl-pretrain"], help='Mode to use')
parser.add_argument('--percent', type=int, choices=[1,5,10,25,50,100], help='Percent to use')
parser.add_argument('--pretrained', type=str, choices=["No","Imagenet","Jigsaw"], help='Model to use')
parser.add_argument('--augmentation', type=str, choices=["yes","no"],default="no", help='augmentation to use')
parser.add_argument('--epochs', type=int,default=30, help='number of epochs to use')
parser.add_argument('--lr', type=float,default=3e-4, help='learning rate to use')
parser.add_argument('--batch_size', type=int,default=512, help='batch size to use')
parser.add_argument("--train_data",type=list,choices=["Delhi","Bangladesh"],help="path to train data")


args = parser.parse_args()
import pickle
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import torchvision.models as models
from torchvision.models import efficientnet_b0
import torchvision.transforms as transforms
from torch.utils.data import DataLoader,Dataset,TensorDataset
import matplotlib.pyplot as plt
import os
print(args.gpu)
os.environ["CUDA_VISIBLE_DEVICES"]= f"{args.gpu}"
import numpy as np
import pandas as pd
import umap.umap_ as umap

# from sklearn.metrics import confusion_matrix,f1_score,accuracy_score,precision_score,recall_score
from astra.torch.metrics import f1_score,accuracy_score,precision_score,recall_score
from sklearn.model_selection import train_test_split, StratifiedKFold
from sklearn.metrics import ConfusionMatrixDisplay
from scipy.spatial.distance import hamming

# ASTRA
from astra.torch.data import load_cifar_10
from astra.torch.utils import train_fn
from astra.torch.models import EfficientNet, MLP, MLPClassifier, EfficientNetClassifier

from itertools import permutations,product

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(device)

result_dict = {}
def get_metrics(y_pred,y_label):
    with torch.no_grad():
        acc = accuracy_score(y_pred,y_label)
        f1 = f1_score(y_pred,y_label)
        precision = precision_score(y_pred,y_label)
        recall = recall_score(y_pred,y_label)
        return acc,f1,precision,recall

def predict(model,X_test,y_test,percent,ssl,batch_size = 512):
    with torch.no_grad():
        model.eval()
        # incorporating batch size
        test_dataset = torch.utils.data.TensorDataset(X_test, y_test)
        test_loader = torch.utils.data.DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
        y_pred = []
        for x, y in test_loader:
            x = x.to(device)
            y = y.to(device)
            output = model(x)
            y_pred.append(output)
        y_pred = torch.cat(y_pred)
        y_pred = torch.argmax(y_pred,dim=1)
        y_pred = y_pred.cpu()
        y_test = y_test.cpu()
        acc,f1,precision,recall = get_metrics(y_pred,y_test)


        result_dict[percent+" "+ssl] = {"accuracy":acc,"f1":f1,"precision":precision,"recall":recall}
        return y_pred

# Test Data
loaded_data = torch.load("/home/rishabh.mondal/Brick-Kilns-project/albk_rishabh/tensor_data_final/test_data.pt")
X_test = loaded_data['images']
y_test = loaded_data['labels']
y_test = y_test.type(torch.LongTensor)
   
# print(args.percent)
# Load Data
if "Bangladesh" in args.train_data:
    loaded_data = torch.load("/home/rishabh.mondal/Brick-Kilns-project/albk_rishabh/tensor_data/new_dataset_Bangladesh_14k.pt")
    X_train = loaded_data['images']
    y_train = loaded_data['labels']

else:  # No Bangladesh data
    X_train = torch.tensor([])
    y_train = torch.tensor([])



if "Delhi" in args.train_data:
    if args.percent == 50:
        loaded_data = torch.load("/home/rishabh.mondal/Brick-Kilns-project/albk_rishabh/tensor_data_final/delhi_data_4500.pt")
        X_train = torch.cat(X_train,loaded_data['images'])
        y_train = torch.cat(y_train,loaded_data['labels'])

    elif args.percent == 25:
        loaded_data = torch.load("/home/rishabh.mondal/Brick-Kilns-project/albk_rishabh/tensor_data_final/delhi_data_2250.pt")
        X_train = torch.cat(X_train,loaded_data['images'])
        y_train = torch.cat(y_train,loaded_data['labels'])
    elif args.percent == 10:
        loaded_data = torch.load("/home/rishabh.mondal/Brick-Kilns-project/albk_rishabh/tensor_data_final/delhi_data_900.pt")
        X_train = torch.cat(X_train,loaded_data['images'])
        y_train = torch.cat(y_train,loaded_data['labels'])
    elif args.percent == 5:
        loaded_data = torch.load("/home/rishabh.mondal/Brick-Kilns-project/albk_rishabh/tensor_data_final/delhi_data_450.pt")
        X_train = torch.cat(X_train,loaded_data['images'])
        y_train = torch.cat(y_train,loaded_data['labels'])
    else:
        loaded_data = torch.load("/home/rishabh.mondal/Brick-Kilns-project/albk_rishabh/tensor_data_final/delhi_data_90.pt")
        X_train = torch.cat(X_train,loaded_data['images'])
        y_train = torch.cat(y_train,loaded_data['labels'])
y_train = y_train.type(torch.LongTensor)


# Model Training and Saving loss and labels, and results

def load_model(pretrained):
    if pretrained == "No":
        model = efficientnet_b0(num_classes=2).to(device)
    elif pretrained == "Imagenet":
        model = efficientnet_b0(pretrained=True)
        model.classifier = nn.Linear(1280,2)
        model = model.to(device)
    elif pretrained == "Jigsaw":
        path = "/home/vannsh.jani/brick_kilns/githubrepo/ML/model_59_delban1.pth"
        model = efficientnet_b0(num_classes=2).to(device)
        model.features.load_state_dict(torch.load(path))
    return model

model = load_model(args.pretrained)


if args.augmentation == "yes":
    s=0.5
    color_jitter = transforms.ColorJitter(0.4*4, 0.4*s, 0.4*s, 0.2*s)
    transform_eval = transforms.Compose([
            # transforms.RandomResizedCrop((224,224), scale=(0.08, 1.0), ratio=(0.75, 1.3333333333333333)),
            transforms.RandomHorizontalFlip(p=0.5),
            transforms.RandomApply([color_jitter], p=0.5),
            transforms.RandomGrayscale(p=0.4),
            transforms.RandomRotation(180),
            # transforms.Resize(224),
            # transforms.ToTensor(),
            # transforms.Normalize((0.4914, 0.4822, 0.4465), (0.2023, 0.1994, 0.2010))
            ])
    X_train = transform_eval(X_train)
    # train_dataset = TensorDataset(X_train, y_train)
    # train_loader = DataLoader(train_dataset, batch_size=512, shuffle=True) 

if args.mode == "fit" or args.mode == "fit-predict":

    iter_losses, epoch_losses = train_fn(model,nn.CrossEntropyLoss(), X_train,y_train, lr=args.lr,verbose=True,batch_size=args.batch_size,epochs=args.epochs)
    plt.plot(iter_losses)
    plt.xlabel("Iteration")
    plt.ylabel("Training loss")
    plt.show()
    path_losses = f"/home/vannsh.jani/brick_kilns/githubrepo/Machine-Learning2/train_loss_{args.percent}_{args.pretrained}_{args.train_data}.pth"
    torch.save(iter_losses,path_losses)
    if args.mode == "fit-predict":
        y_pred = predict(model,X_test,y_test,f"{args.percent}%",f"{args.pretrained}_{args.train_data}")
        # save results
        result_path = f"/home/vannsh.jani/brick_kilns/githubrepo/Machine-Learning2/results_{args.percent}_{args.pretrained}_{args.train_data}.pth"
        pickle.dump(result_dict,open(result_path,"wb"))
        labels_path = f"/home/vannsh.jani/brick_kilns/githubrepo/Machine-Learning2/labels_{args.percent}_{args.pretrained}_{args.train_data}.pth"
        pickle.dump(zip(y_pred,y_test),open(labels_path,"wb"))
    # saving model weights
    features_path = f"/home/vannsh.jani/brick_kilns/githubrepo/ML/features_{args.percent}_{args.pretrained}_{args.train_data}.pth"
    torch.save(model.features.state_dict(),features_path)
    classifier_path = f"/home/vannsh.jani/brick_kilns/githubrepo/ML/classifier_{args.percent}_{args.pretrained}_{args.train_data}.pth"
    torch.save(model.classifier.state_dict(),classifier_path)

# Model Evaluation
elif args.mode=="predict":
    features_path = f"/home/vannsh.jani/brick_kilns/githubrepo/ML/features_{args.percent}_{args.pretrained}_{args.train_data}.pth"
    model.features.state_dict(torch.load(features_path))
    classifier_path = f"/home/vannsh.jani/brick_kilns/githubrepo/ML/classifier_{args.percent}_{args.pretrained}_{args.train_data}.pth"
    model.classifier.state_dict(torch.load(classifier_path))
    y_pred = predict(model,X_test,y_test,f"{args.percent}%",f"{args.pretrained}_{args.train_data}")
    # save results
    result_path = f"/home/vannsh.jani/brick_kilns/githubrepo/Machine-Learning2/results_{args.percent}_{args.pretrained}_{args.train_data}.pth"
    pickle.dump(result_dict,open(result_path,"wb"))
    labels_path = f"/home/vannsh.jani/brick_kilns/githubrepo/Machine-Learning2/labels_{args.percent}_{args.pretrained}_{args.train_data}.pth"
    pickle.dump(zip(y_pred,y_test),open(labels_path,"wb"))

else:
    # SSL Pretraining
    # Resizing images
    X_train = F.interpolate(X_train, size=(225, 225), mode='bilinear', align_corners=False)
    X_test = F.interpolate(X_test, size=(225, 225), mode='bilinear', align_corners=False)

    X_pool = torch.cat([X_train,X_test])
    y_pool = torch.cat([y_train,y_test])

    # Divinding image into 9 patches
    def divide_into_patches(images):

        patches = torch.split(images,75,dim=3)
        # print(patches[0].shape)
        patches = [torch.unsqueeze(patch,1) for patch in patches]
        # print(patches[2].shape,len(patches))
        patches = torch.cat(patches,dim=1)
        patches = torch.split(patches,75,dim=3)
        patches = torch.cat(patches,dim=1)

        return patches


    images_with_patches = divide_into_patches(X_pool)

    def top_k_hamming(k):
        # find k permutations with highest hamming distance
        permuts_list = list(permutations(range(9)))
        permuts_array = np.array(permuts_list)
        no_permuts = len(permuts_list)

        permuts_to_take = k
        set_of_taken = set()
        cnt_iterations = 0
        while True:
            cnt_iterations += 1
            x = np.random.randint(0, no_permuts )
            y = np.random.randint(0, no_permuts )
            permut_1 = permuts_array[x]
            permut_2 = permuts_array[y]
            hd = hamming(permut_1, permut_2)

            if hd > 0.9 and (not x in set_of_taken) and (not y in set_of_taken):
                set_of_taken.add(x)
                set_of_taken.add(y)

                if len(set_of_taken) == permuts_to_take:
                    break

            # if cnt_iterations % 100 == 0:
            #     print ("Already performed count of iterations with pairs of jigsaw permutations", cnt_iterations)
            #     print ("Length of set of taken: ",len(set_of_taken))

        # print ("No of iterations it took to build top - {} permutations array = {}".format(permuts_to_take, cnt_iterations))
        # print ("No of permutations", len(set_of_taken))
        selected_permuts = []
        for ind, perm_id in enumerate(set_of_taken):
            selected_permuts.append(permuts_array[perm_id])
        selected_permuts = np.array(selected_permuts)
        selected_permuts = torch.tensor(selected_permuts)
        return selected_permuts
        
    selected_permuts = top_k_hamming(64)


    def get_rand_perms(nperms,selected_perms):
        rand_idx = torch.randint(0, len(selected_perms), (nperms,))
        return selected_perms[rand_idx],rand_idx

    rand_perms,y_labels = get_rand_perms(len(X_train)+len(X_test),selected_permuts)

    def rearrange_patches(images_with_patches,random_permutations):

        images_with_patches_rearranged = torch.zeros(images_with_patches.shape)
        for i in range(images_with_patches.shape[0]):
            img = images_with_patches[i]
            img_rearranged = img[random_permutations[i]]
            images_with_patches_rearranged[i] = img_rearranged

        return images_with_patches_rearranged

    permuted_images = rearrange_patches(images_with_patches,rand_perms)

    model = models.efficientnet_b0(pretrained=False).to(device)
    aggregator = MLPClassifier(9000,[1280,1024,256],n_classes=64).to(device)

    def train_ssl_model(model,aggregator, loss_fn, images, labels, lr=3e-4, batch_size=512, epochs=50, verbose=True):
    
        iter_losses = []
        epoch_losses = []

        model.train()
        aggregator.train()
        # optimizer = torch.optim.Adam(model.parameters(), lr=lr)
        optimizer = torch.optim.Adam(list(model.parameters())+list(aggregator.parameters()), lr=lr)
        for epoch in range(epochs):
            for i in range(0, len(images), batch_size):
            
                p1, p2, p3, p4,p5,p6,p7,p8,p9 = images[i:i + batch_size][:, 0], images[i:i + batch_size][:, 1], images[i:i + batch_size][:, 2], images[i:i + batch_size][:, 3],images[i:i + batch_size][:, 4],images[i:i + batch_size][:, 5],images[i:i + batch_size][:, 6],images[i:i + batch_size][:, 7],images[i:i + batch_size][:, 8]
                p1,p2,p3,p4,p5,p6,p7,p8,p9 = p1.to(device),p2.to(device),p3.to(device),p4.to(device),p5.to(device),p6.to(device),p7.to(device),p8.to(device),p9.to(device)
                flat_labels = labels[i:i + batch_size]
                flat_labels = flat_labels.type(torch.LongTensor)
                patches = [p1,p2,p3,p4,p5,p6,p7,p8,p9]
                patch_out = []
                for patch in patches:
                    patch_out.append(model(patch))
                patch_out = torch.cat(patch_out,dim=-1)
                y_pred_prob = aggregator(patch_out)
                # y_pred_prob = model(p1,p2,p3,p4,p5,p6,p7,p8,p9)
                loss = loss_fn(y_pred_prob, flat_labels.to(device))
                loss.backward()
                optimizer.step()
                optimizer.zero_grad()
                iter_losses.append(loss.item())


            epoch_losses.append(loss.item())
            if verbose:
                print(f"Epoch {epoch + 1}/{epochs}, loss={loss.item():.4f}")
            if epoch % 10 == 0 and epoch != 0 or epoch == epochs - 1:
                # save parameters
                path = f"/home/vannsh.jani/brick_kilns/githubrepo/ML/model_{epoch}_delban1.pth"
                # path_a = f"/home/vannsh.jani/brick_kilns/githubrepo/ML/aggregator_{epoch}_delban1.pth"
                torch.save(model.features.state_dict(), path)
                # torch.save(aggregator.state_dict(), path_a)

        return iter_losses, epoch_losses
    
    iter_losses, epoch_losses = train_ssl_model(model,aggregator,nn.CrossEntropyLoss(),permuted_images.to(device),y_labels.to(device),lr=3e-4,
                                     batch_size=256, epochs=60, verbose=True)
    



    







