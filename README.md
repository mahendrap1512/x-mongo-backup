This script will help you to create multiple backup of your mongodb at different time.
Some use case are you can use this script to run as a cron job,
or you can manually run this script with  `python manager.py`
## Prerequisite
1. mongodb must be installed on your system.
2. Python3 must be installed on your system.

### Configuration
Add your configuration in `config.json` file.

1. LIMIT is maximum number of backup you want to retain.
2. BACKUP_DIR is where your backup will be found.
3. HISTORY  is where logs of removed directory with time can be found.
4. DATABASE is name of your database.
5. URI must be in this format     ```mongodb+srv://<username>:<password>@cluster0.bmggr.mongodb.net/<database_name>``` , which you can found in your mongo-atlas account.

### How to use ?
1. Download these files
2. change `config.json` with proper configuration according to you mongo database.
3. Run `python manager.py`
