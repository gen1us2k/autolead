
DROPLAB – help you to automatize making issue with attaches on gitlab

   
RUN

you have no need to install program

you can run it with  console "python drolab.py" command

for total form of console input you need to type

droplab [OPTIONS]

OPTIONS

    --dropbox_token					Dropbox private token
    --gitlab_token					Gitlab private token
    -f				--file			File to upload gitlab.com
    -p				--project		Project id where you will upload file
    -t				--title			Title for new issue
   


python drolab.py --gitlab_token your_token --file filename.format --project project_number --title title_of_yout_issue --dropbox_token token_on_dropbox

for example:

python gitlab_board_issue.py --gitlab_token fdgdsJHJnH8fyMh --file rat.py --project 4067343 --title Issue --dropbox_token JHJHHJHHHJDHDJSBfadr-oQlRdg55-B90eTItbj0SyEJKHJH787BBaY
