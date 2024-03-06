# Avrae Utilities for PyCharm
A runnable configuration for [Pycharm](https://www.jetbrains.com/pycharm/) for the [Avrae](https://avrae.io/) Discord bot

## Important Note
This package makes a remote connection to the Avrae API in order to collect and update the information. It only does this by request, and will not make any outward connection without being prompted to by the user.

## Setup

### Getting the Application
It is recommended to use Git to get this project, otherwise you will need to download and add the project to the repo you manage your aliases in.

To download this application
1. Open the terminal in PyCharm and type ``git submodule add https://github.com/Corvux89/Avrae-Pycharm <optional_submodule_path>``. If you don't specify the submodule path it will just add it to the root directory.
2. Add a configuration to run `app.py`.
3. Ensure you have the parameter of `$FilePath$`
![PyCharm Configuration](https://i.imgur.com/o7h4TIO.png)

#### Environment Variables
| Name              | Description                                                                     | Required? |
|-------------------|---------------------------------------------------------------------------------|-----------|
| `AVRAE_TOKEN`     | Secret Avrae token for discord                                                  | **Yes**   |
|`FILE_DEPTH`       | How many levels of directories to look through to find the `collection.io` file | No        |

#### Getting the AVRAE_TOKEN
In order for this plugin to have your permissions to grab and update your GVARs, Workshop Aliases, or Workshop Snippets, you need to give it your token.

1. Setup a run configuration in PyCharm to run the ``avrae.py`` file
2. Go to [Avrae](https://avrae.io) and log in to the dashboard
3. Press F12 to open the DevTools
4. Go to the 'Application' tab
5. On the left, select 'https://avrae.io' under 'Local Storage'
6. Copy the 'Value' next to the 'AVRAE_TOKEN' key

#### Updating the project
In the future if there are updates to the application you want to get you can either copy/paste or run
`git submodule update --remote --merge` to pull updates from github

### Note
Please keep this token private, as anyone who gains access to this token could potentially gain access to your Discord account.

## Features

#### Get Collection Information
You can use the ``Pull New Collection Data`` button to collect a json of all of the aliases and snippets ids within a collection. This expects the collection ID. You can find this by going to the collection on the Workshop, and looking at the url. Everything after ``avrae.io/dashboard/workshop/`` is your ID.

Once you've ran the ``Pull New Collection Data`` command, save the result as `collection.id` in the folder you wish to save your collection in. This will also automatically download the collection description if the collection has one and save it in a `readme.md`

Now that you have the `collection.id` anytime you run this updator in the directory it resides, it will assume we are working with this collection.

#### Updating 
When working within a collection file, if this application is set to the default configuration you can hit `shift + f10` to run it. It will prompt for what you want to do.

1. Push Update -> Select this or hit `1` to push an update. It will handle checking if this is a snippet, alias, or markdown descriptions for an alias, snippet, or the collection itself 
2. Pull Update -> Select this or hit '2' to update the selected file with the latest version of information on the Workshop. Works with snippets, aliases, gvars, and markdown files

`Pull Alias` -> Will prompt you to select an alias to download. This will create a `.alias` and `.md` file
`Pull Snippet` -> Will prompt you to select a snippet to download. This will create a `.alias` and `.md` file
`Pull GVAR` -> Will prompt you to select a GVAR to download. This will create a `.alias` and `.md` file
`Main Menu` -> Back to the initial setup screen where you can either pull a new collection, or update the current `collection.io` file

#### Folder Structure
Support for editing the documentation will come in a future update.

Here is an example collection folder structure:
```bash
root
 | # This is the folder your collection will live in
 ├ Collection Name
 | | # This contains the json collected by the `Get Collection Data` command
 | ├ collection.id 
 | | # This contains the markdown for the collection description
 | ├ readme.md 
 | | # This contains the alias itself, collected by the `Get Workshop Alias` command, and updated with the `Update Workshop Alias` command
 | ├ aliasName.alias 
 | | # This contains the markdown the alias description
 | ├ aliasName.md 
 | | # This contains the subalias alias itself, collected by the `Get Workshop Alias` command, and updated with the `Update Workshop Alias` command
 | ├ aliasName subAalias.alias 
 | | # This contains the markdown the alias description
 | ├ aliasName subAalias.md 
 | | # This contains the snippet itself, collected by the `Get Workshop Snippet` command, and updated with the `Update Workshop Snippet` command
 | ├ snippetName.snippet 
 | | # This contains the markdown the snippet description
 | └ snippetName.md 
```