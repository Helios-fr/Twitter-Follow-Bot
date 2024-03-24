## This is the /keys directory
This direcotry contains files associated with the acconts used in the application, this directory is empty by default and all files in this directory that end in .secret are ignored by git and will not be uploaded to any repository on github.

## Adding a new account
1. First create a new file in this directory with the name of the account you want to add, in the format of `accountname.secret`
2. Add the account cookies to the file in the following format can be retrieved from the browser console from the storage tab, simply right click on the cookie and copy the value.
```
ct0 = {ct0 cookie}
auth_token = {auth_token cookie}
```
3. Save the file and run the application, the account will be automatically added to the application and will be used for any future actions.