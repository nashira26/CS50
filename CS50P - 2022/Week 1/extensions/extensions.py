file_name = input("File name: ").lower().strip().split(".")


ext = file_name[-1]
if ext == "gif":
    print("image/gif")
elif ext == "jpg" or ext == "jpeg":
    print("image/jpeg")
elif ext == "png":
    print("image/png")
elif ext == "pdf":
    print("application/pdf")
elif ext == "txt":
    print("text/plain")
elif ext == "zip":
    print("application/zip")
else:
    print("application/octet-stream")



