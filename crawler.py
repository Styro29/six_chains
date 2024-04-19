# crawler.py

from langchain_community.document_loaders import UnstructuredURLLoader
import os.path
import pickle

class Crawler:
    def get_data_from_url(self, url_file="urls.txt", save_dir=os.path.dirname(__file__)):
        filename = "text_data"
        filename_check = "text_data_check.txt"
        save_path = os.path.join(save_dir, filename)
        save_path_check = os.path.join(save_dir, filename_check)
        
        with open(url_file, 'r', encoding='utf-8') as url_list:
            urls = [url.strip() for url in url_list]
            
        if os.path.isfile(save_path):
            print(f"Text data file found for {filename}\n >>>>> Loading... <<<<<")
            with open(save_path, 'rb') as fp:
                data = pickle.load(fp)
                return data
        else:
            print(f"Text data file not found for {filename}\n >>>>> Downloading... <<<<<")
            url_loader = UnstructuredURLLoader(urls=urls)
            text_data = url_loader.load()
                    
            if text_data is None:
                print(f"Error: Failed to load text data from URLS.")
                return
            else:
                with open(save_path, 'wb') as fp:
                    pickle.dump(text_data, fp)
                print(f">>>>> Text data saved for urls to {save_path} <<<<<")
                        
                with open(save_path_check, 'w', encoding='utf-8') as f:
                    for item in text_data:
                        f.write(str(item) + "\n")
                print(f">>>>> Text data saved for urls to {save_path_check} <<<<<")    
            return text_data