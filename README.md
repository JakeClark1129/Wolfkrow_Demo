# Wolfkrow_Demo
Simple Wrapper app around Wolfkrow to highlight the framework's capabilities. 

## Setup

1. Ensure that you have Wolfkrow installed. To do this, you can download the latest version from GitHub, and then pip install the zip file.
    Wolfkrow GitHub: https://github.com/JakeClark1129/Wolfkrow/tags
    Pip command: `pip install <path-to-wolfkrow.zip>`

2. Download or Clone this demo Git Repo

3. Set the WOLFKROW_DEMO_ROOT environment variable to the path to the downloaded demo folder.

4. ensure that the scripts folder is added to PATH.
    `<repo_root>/_software/scripts`

5. Set the Wolfkrow environment variables.
    * Path to your python executable. `WOLFKROW_DEFAULT_COMMAND_LINE_EXECUTABLE: C:/Program Files/python/3.9.13/python.exe`
    * Path to the wolfkrow_run_task python script. `WOLFKROW_DEFAULT_COMMAND_LINE_EXECUTABLE_ARGS: C:/Projects/Wolfkrow/src/wolfkrow/scripts/wolfkrow_run_task.py`
        * NOTE: If on windows, pip may create a wolfkrow_run_task.exe file. This should work in place of the python executable, and you can exclude the args environment variable.

    * The path to the wolfkrow.yaml file provided with the demo. `WOLFKROW_CONFIG_SEARCH_PATHS: <repo_root>/_config/wolfkrow.yaml`

6. For the Nuke Publish app, ensure the nuke_startup folder is added to NUKE_PATH
    <repo_root>/_software/src/nuke_startup


# How to run the apps

If you've not already, watch the introduction video to see the ingest app in action.
https://youtu.be/kKVP9gBREfo

After the set up is complete, you should be able to run the apps. You must start with the ingest app, since it is 
responsible for creating the plates which should be used in the Comp Publish/Client Delivery app. 

## Ingest

1. Open a shell (Such as Bash for Mac/Linux, or PowerShell for Windows)
2. Run the ingest script.
    A. It takes an argument to the folder containing the image sequences you want to ingest. 

Ex:
`ingest.bat <repo_root>/shows/demo_show/client_io/in/2025_10_30/package_13`

NOTE: The ingest app is set up to expect a specific naming convention of the plates. If you are not using the demo files 
    provided, it my not recognize them unless you re-create the naming convention perfectly. If you want to set up a more
    bespoke pipeline, please feel free to reach out and I can help.

## Publish

1. Read the ingested plates into nuke
2. Create a simple comp
3. Render the comp
4. Run the `Publish -> Publish Selected Write Nodes` app from the top menu bar.

You can check the terminal that opened with Nuke for the progress, or look via the log in the script editor afterwards to see how the process completed.

## Client Deliver

1. Open a shell (Such as Bash for Mac/Linux, or PowerShell for Windows)
2. Run the deliver script. It takes 2 arguments:
    A: The path to the first frame of the image sequence you want to publish.
    B. the Export Option you want to use, which is the name of the workflow you want to process the sequence through. 

Ex:
deliver.bat <repo_root>/shows/demo_show/shots/999_rnd/999_rnd_999/publish/comp/Write1/v001/render/999_rnd_999_Write1_v001.1001.exr --export_option "Demo Client Export - Movs"
