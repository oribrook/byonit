import requests
import base64


def decode_credentials(username, password):
    return base64.b64encode(bytes(f"{username}:{password}",
 						 "ISO-8859-1")).decode("ascii")


if __name__ == "__main__":

    ###################
    # what to test?
    create_user = False
    create_post = False
    delete_post = False
    edit_post = True

    ###################
    # test config:    
    user = "ori"
    pw = "123"
    email = "moshe@123.com"
    title = "some title "
    content = "some content"
    new_title = "new edited title"
    new_content = "new edited content"
    post_id = 3

    # credentials (for base64 auth)
    cred_data = {'Authorization': f'Basic {decode_credentials(user, pw)}'}

    #############################################################################
    #############################################################################
    # create user:

    if create_user:
        res = requests.post("http://127.0.0.1:8000/api/v1/signup", 
                            {'username': user, 'password': pw, "email": email})

        assert res.status_code == 200, f"create user issue. {res.text}"
        print(res.text)

    #############################################################################
    #############################################################################
    # create post 

    if create_post:                
        res = requests.post(url="http://127.0.0.1:8000/api/v1/post-auth",
                    headers=cred_data, 
                    data={"title": title, "content": content})

        assert res.status_code == 200, f"create post issue. {res.text}"
        print(res.text)
    
    #############################################################################
    #############################################################################
    # delete post by owner
    
    if delete_post:                
        res = requests.delete(url="http://127.0.0.1:8000/api/v1/post-auth",
                    headers=cred_data, 
                    data={"id": post_id})
        
        assert res.status_code == 200, f"delete post issue. {res.text}"
        print(res.text)

    #############################################################################
    #############################################################################
    # edit post

    if edit_post:        
        res = requests.put(url="http://127.0.0.1:8000/api/v1/post-auth",
                    headers=cred_data, 
                    data={"id": post_id, "title": new_title, 
                          "content": new_content})
        
        assert res.status_code == 200, f"edit post issue. {res.text}"
        print(res.text)


    # filtering & ordering
    # http://127.0.0.1:8000/api/v1/posts?author=ori&created_at=2023-11-26
    # http://127.0.0.1:8000/api/v1/posts?author=moshe
    # http://127.0.0.1:8000/api/v1/posts?created_at=2023-11-26
    # http://127.0.0.1:8000/api/v1/posts?sort_by=creation
    # http://127.0.0.1:8000/api/v1/posts?sort_by=modification
