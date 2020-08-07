import sys, os
from skillshare import Skillshare, splash
# from magic import cookie

# or by class ID:
# dl.download_course_by_class_id(189505397)
cookie = """
device_session_id=d998790a-8850-4a2b-8fae-01f30ae79548; show-like-copy=0; visitor_tracking=utm_campaign%3D%26utm_source%3D%26utm_medium%3D%26referrer%3Dhttps%3A%2F%2Fwww.skillshare.com%2Flogin%26referring_username%3D; first_landing=utm_campaign%3D%26utm_source%3D%26utm_medium%3D%26referrer%3Dhttps%3A%2F%2Fwww.skillshare.com%2Flogin%26referring_username%3D; _gcl_au=1.1.1293509713.1594595739; sm_uuid=1594596345736; __stripe_mid=8b4d0467-88a9-4532-9869-4560b9e7eb68; _scid=9c446879-9b20-4a4f-8093-357b3d2f6880; _pin_unauth=dWlkPU5ERTFNVEE1TkRjdE1XVTNNaTAwT1RoakxXSTVOekl0TUdReVltTmhOR1F4TnpVNQ; __qca=P0-836559679-1594595739427; G_ENABLED_IDPS=google; __utmv=99704988.|1=visitor-type=user=1; __pdst=26be828663ed42d6b0031b32d3653a8f; __ssid=c36c642257d77f5388301ed0afbb7e8; __utmz=99704988.1594904003.3.2.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); skillshare_user_=ba9e8969fb87a67e2228358a5bc1cbc6b1468ff2a%3A4%3A%7Bi%3A0%3Bs%3A8%3A%2214623770%22%3Bi%3A1%3Bs%3A23%3A%22arrian.marlo%40andyes.net%22%3Bi%3A2%3Bi%3A2592000%3Bi%3A3%3Ba%3A11%3A%7Bs%3A5%3A%22email%22%3Bs%3A23%3A%22arrian.marlo%40andyes.net%22%3Bs%3A9%3A%22firstName%22%3Bs%3A2%3A%22Al%22%3Bs%3A8%3A%22lastName%22%3Bs%3A6%3A%22Nejati%22%3Bs%3A8%3A%22headline%22%3BN%3Bs%3A3%3A%22pic%22%3Bs%3A68%3A%22https%3A%2F%2Fstatic.skillshare.com%2Fassets%2Fimages%2Fdefault-profile-2020.jpg%22%3Bs%3A5%3A%22picSm%22%3Bs%3A68%3A%22https%3A%2F%2Fstatic.skillshare.com%2Fassets%2Fimages%2Fdefault-profile-2020.jpg%22%3Bs%3A5%3A%22picLg%22%3Bs%3A68%3A%22https%3A%2F%2Fstatic.skillshare.com%2Fassets%2Fimages%2Fdefault-profile-2020.jpg%22%3Bs%3A9%3A%22isTeacher%22%3Bs%3A1%3A%220%22%3Bs%3A8%3A%22username%22%3Bs%3A8%3A%2294053767%22%3Bs%3A3%3A%22zip%22%3BN%3Bs%3A6%3A%22cityID%22%3Bs%3A1%3A%220%22%3B%7D%7D; PHPSESSID=f3dd8066810289d97c9f6e3045496836; YII_CSRF_TOKEN=MWNMb0NKbTZMMzNjTnFSNG9SUjJuMW52ektYcnladUgnRr6JHnNBTXrFkVFahWtXl39pGsg84rbBVcNQeuTnOA%3D%3D; __stripe_sid=93d07e96-c442-45a8-b99b-bf44cc8afac6; _uetsid=494fa1fb10c26e79595b8792e3b0918d; _uetvid=344b7bfe60f2f2b8bfa2277bf1355e3c; IR_gbd=skillshare.com; IR_4650=1595149044597%7C0%7C1595149044597%7C%7C; IR_PI=c924905a-bd88-11ea-8fad-0295e3e6ea6a%7C1595235444597; __utma=99704988.385405741.1594595739.1594904003.1595149046.4; __utmc=99704988; __utmt=1; __utmb=99704988.1.10.1595149046; _sctr=1|1595100600000; _derived_epik=dj0yJnU9ZFJUQnhLdF9CeEgzOUxoMWtKaXdnVVVtTlE1emgwaFQmbj1Jem45Qm1DYlg1amxoNHVsUTJ3UVF3Jm09MSZ0PUFBQUFBRjhVQ3FZJnJtPTEmcnQ9QUFBQUFGOFVDcVk
"""

def main():
    dl = Skillshare(cookie)
    course_url = sys.argv[1]
    dl.download_course_by_url(course_url)


if __name__ == "__main__":
    splash()
    main()
