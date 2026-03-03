import kagglehub
import shutil
import os
# Download latest version
# import opendatasets as od

# path = kagglehub.dataset_download("maxwell201/clothing-sales-data")
path = kagglehub.dataset_download("aliiihussain/amazon-sales-dataset")


current_dir = os.getcwd()
shutil.copytree(path, os.path.join(current_dir, "amazon_sls"), dirs_exist_ok=True)

print("Path to dataset files:", path)



# # This downloads and unzips the dataset into the current directory
# os.download("https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce")