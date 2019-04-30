##Steps
```
1.Load test images into azure vm.
2.Generate the image tags and other features using cognitive vision api.
3.Persist the image location in the json response generated in step2.
4.Copy the output json to azureblob.
5.Run a Datafactory pipeline to load blob data to cosmos document db.
6.Query the cosmos db to match the image critera.
```
