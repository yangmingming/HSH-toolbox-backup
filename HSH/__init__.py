##encoding=utf8
"""
If you run this file as the main script.
Then package "HSH" will be installed for all Python version you have installed
"""
from __future__ import print_function

__all__ = ["LinearSpider"]

if __name__ == "__main__":
    import os, shutil
    
    def install_HSH():
        """
        This script is to install the HSH package to all installed python version
        """
        # get installed python information
        py2_folders, py3_folders = list(), list()
        for _, folders, _ in os.walk(r"C:\\"):
            for folder in folders:
                if folder.startswith("Python2"):
                    py2_folders.append(folder)
                elif folder.startswith("Python3"):
                    py3_folders.append(folder)
                    
            print("For Py2x You have installed %s." % py2_folders)
            print("For Py3x You have installed %s." % py3_folders)
            break
        
        # remove existing temporary files
        print("\nRemoving existing __pycache__ folder and .pyc files")
        folder_to_be_delete, fname_to_be_delete = list(), list()
        for root, folders, fnames in os.walk(os.getcwd()):
            if os.path.basename(root) == "__pycache__": # if is cache folder
                folder_to_be_delete.append(root) # add to to-delete list
            for fname in fnames:
                if fname.endswith(".pyc"): # if is pre-compile file
                    fname_to_be_delete.append(os.path.join(root, fname)) # add to to-delete list
        
        for folder in folder_to_be_delete:
            shutil.rmtree(folder)
        for fname in fname_to_be_delete:
            try:
                os.remove(fname)
            except:
                pass
            
        # remove currently installed HSH packages and 
        # copy file to site-packages in all python versions
        for pyroot in py2_folders + py3_folders:
            dst = os.path.join("C:\\", pyroot, r"Lib\site-packages\HSH")
            try: # remove
                print("Deleting %s" % dst)
                shutil.rmtree(dst)
            except:
                pass
             
            print("Copying file to %s..." % dst) # copy to
            shutil.copytree(os.path.abspath(os.getcwd() ), 
                            dst)
         
    install_HSH()