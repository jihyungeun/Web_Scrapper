import requests

indeed_result = requests.get("https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=%EC%A0%95%EB%B3%B4%EB%B3%B4%EC%95%88&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=any&limit=50&sort=&psf=advsrch&from=advancedsearch")

print(indeed_result)
