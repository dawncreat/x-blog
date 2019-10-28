# Description

## what is X_BLOG
----------
X_BLOG is going to a be web application which not only support bloging but also
other useful staff.

## feathures going to be obtained
----------
* basic blog feathures
  * able to create and modify article tags
  * upload your article or write your article online and relate your articles
    to your tags.
  * modify your articles when you've finished your articles
  * guests logined in or not could comment your articles
  * able to edit comments about your articles
  * display the count of the article read
  * display the count of users who visits your article
  * display a picture of regines of people who visit your websites.
  * able to search your articles from your site by name
  * able to sort the search result by create time or edit time or tags
  * able to share this article
* markdown editor support
* boostnote translation
* support emoji
* ...

## documents

## deploy
### start a mysql container
before that you should make docker enabled
```shell
docker run -p 3306:3306 --name X_Blog -e MYSQL_ROOT_PASSWORD=root -d mysql:latest

docker exec -u root -it X_Blog mysql -uroot -proot

GRANT ALL ON *.* TO 'root'@'0.0.0.0';
GRANT ALL ON *.* to 'root'@'%' IDENTIFIED BY 'root'; 

mysql 8
GRANT ALL PRIVILEGES on *.* to 'root'@'%';
ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root';


FLUSH PRIVILEGES
```
## contribute

# Welcome

# Get in touch
