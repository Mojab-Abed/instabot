from instapy import InstaPy

main = InstaPy(username="pytest_ma", password="m0g4bab33d" , headless_browser=True)
main.login()
db = ['m.ojab','its.mojab']
main.follow_by_list(db)