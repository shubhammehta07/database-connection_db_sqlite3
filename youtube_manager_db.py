import sqlite3
con=sqlite3.connect('youtube_videos.db')
cursor=con.cursor()


def list_of_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_videos(name,time):
    cursor.execute("INSERT INTO videos (name,time)VALUES (? ,?)",(name,time))
    con.commit()
def update_videos(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name=?,time=? WHERE id=?",(new_name,new_time,video_id))
    con.commit()

def delete_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id=?",(video_id,))
    con.commit()
cursor.execute(''' 
        CREATE TABLE  IF NOT EXISTS videos(
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL 
        )        
''')


def main():
    while True:
        print('\n')
        print('Youtube manager with sqlite3 DB')
        print("1.List of Videos")
        print("2.Add Videos")
        print("3.Update Videos")
        print("4.Delete Videos")
        print("5.Exit App")
        choice=input('Enter your option :- ')
        if choice =='1':
            print('\n')
            print('*'*50)
            list_of_videos()
            print('\n')
            print('*'*50)
        elif choice=='2':
            name=input('Enter video name :- ')
            time=input('Enter video duration time :- ')
            add_videos(name,time)
        elif choice =='3':
            video_id=input('Enter video id to update :- ')
            name=input('Enter video name :- ')
            time=input('Enter video duration time :- ')
            update_videos(video_id,name,time)
        elif choice =='4':
            video_id=input('Enter video id to delete:- ')
            delete_videos(video_id)
        elif choice =='5':
            break
        else:
            print("Invalid option")
    con.close()


if __name__=="__main__":
    main()
