import urllib.request

import  os

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/example1.txt"
filename = "example1.txt"

try:
    urllib.request.urlretrieve(url, filename)
    if os.path.exists(filename):
        print("File downloaded successfully!")

        print("File size:", os.path.getsize(filename), "bytes")
        print("File path:", os.path.abspath(filename))

        with open(filename, "r" , encoding="utf-8") as f:
            print("File mode:" , f.mode)

            content = f.read()
            
            print("File conttent:")
            print(content)

            print("Type of content:", type(content))

            print("Content with new line:")
            print(content.replace("\\n", "\n"))





except Exception as e:
    print("Error:", e)



