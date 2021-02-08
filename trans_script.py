import pydicom
import uuid
import random
import os
import argparse
import math

parser = argparse.ArgumentParser()

#命令行
parser.add_argument("-d", "--data_dir", type=str, required=True, help="input images dir")
parser.add_argument("-s", "--save_dir", type=str, required=True, help="save images dir")
args = parser.parse_args()

def main():

    name_dict = {}
    age_dict = {}
    weight_dict = {}
    birth_dict = {}
    sex_dict = {}
    id_dict = {}
    ins_add_dict = {}
    ins_name_dict = {}

    if not os.path.exists(args.save_dir):
        os.makedirs(args.save_dir)

    dir_list = os.listdir(args.data_dir)
    for sub in dir_list:
        read_path = os.path.join(args.data_dir, sub)#sub是文件夹里面的目录，这里设定只有dicom格式才可读
        print(sub)
        try:
            ds = pydicom.read_file(read_path)

            if "PatientName" in ds and ds.PatientName not in name_dict:
                name_dict[ds.PatientName]=str(uuid.uuid1())
            if "PatientAge" in ds and ds.PatientAge not in age_dict:
                age_dict[ds.PatientAge] = str(uuid.uuid1())
            if "PatientWeight" in ds and ds.PatientWeight not in weight_dict:             
                weight_dict[ds.PatientWeight] = str(math.exp(float(ds.PatientWeight)))
            if "PatientBirthDate" in ds and ds.PatientBirthDate not in birth_dict:
                birth_dict[ds.PatientBirthDate] = str(uuid.uuid1())
            if "PatientSex" in ds and ds.PatientSex not in sex_dict:
                sex_dict[ds.PatientSex] = str(uuid.uuid1())
            if "PatientID" in ds and ds.PatientID not in id_dict:
                id_dict[ds.PatientID] = str(uuid.uuid1())
            if "InstitutionAddress" in ds and ds.InstitutionAddress not in ins_add_dict:
                ins_add_dict[ds.InstitutionAddress] = str(uuid.uuid1())
            if "InstitutionName" in ds and ds.InstitutionName not in ins_name_dict:
                ins_name_dict[ds.InstitutionName] = str(uuid.uuid1())
            # 修改ds内容
            if "PatientName" in ds:
                ds.PatientName = name_dict[ds.PatientName]
            if "PatientAge" in ds:
                ds.PatientAge = age_dict[ds.PatientAge]
            if "PatientWeight" in ds:
                ds.PatientWeight = weight_dict[ds.PatientWeight]
            if "PatientBirthDate" in ds:
                ds.PatientBirthDate = birth_dict[ds.PatientBirthDate]
            if "PatientSex" in ds:
                ds.PatientSex = sex_dict[ds.PatientSex]
            if "PatientID" in ds:
                ds.PatientID = id_dict[ds.PatientID]
            if "InstitutionAddress" in ds:
                ds.InstitutionAddress = ins_add_dict[ds.InstitutionAddress]
            if "InstitutionName" in ds:
                ds.InstitutionName = ins_name_dict[ds.InstitutionName]
            
            save_path = os.path.join(args.save_dir, sub)
            ds.save_as(save_path)

    
        except:
            print("[ERROR] 文件{}不是可读取文件".format(sub))
    
    # 保存txt
    txt_path = os.path.join(args.save_dir, 'txt_dir')
    if not os.path.exists(txt_path):
        os.makedirs(txt_path)

    def write_txt(name, content):
        f_path = os.path.join(txt_path, name)
        fw = open(f_path,'w+')
        fw.write(str(content))
        fw.close()

    write_txt("PatientName.txt", name_dict)
    write_txt("PatientAge.txt", age_dict)
    write_txt("PatientWeight.txt", weight_dict)
    write_txt("PatientBirthDate.txt", birth_dict)
    write_txt("PatientSex.txt", sex_dict)
    write_txt("PatientID.txt", id_dict)
    write_txt("InstitutionAddress.txt", ins_add_dict)
    write_txt("InstitutionName.txt", ins_name_dict)

if __name__ == "__main__":
    main()


    