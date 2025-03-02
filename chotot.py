import requests
import json
import time
list_old = []
i = 0
vong = 3180
res = requests.get("https://www.chotot.com/mua-ban-phu-kien?f=p&page=1&price=0-1000000")
output = res.content.decode()
output_res = output.split(r'script id="__NEXT_DATA__" type="application/json">')[1].split(r"</script>")[0]
while True:
    try:
        i+= 1
        vong+=1
        res = requests.get("https://www.chotot.com/mua-ban-phu-kien?f=p&page=1&price=0-1000000")
        output = res.content.decode()
        output_res = output.split(r'script id="__NEXT_DATA__" type="application/json">')[1].split(r"</script>")[0]
        output_json = json.loads(output_res)
        # with open("./file.json","w",encoding="utf-8") as i:
        #     json.dump(output_json,i)
        listPost = output_json["props"]["initialState"]["adlisting"]["data"]["ads"]
        for post in listPost:
            kt = 0
            link = "https://www.chotot.com"
            if post["region_name"] == "Tp Hồ Chí Minh":
                print("vao")
                for old_post in list_old:
                    print("ok")
                    if old_post == post["subject"]:
                        kt =1
                        print("ok")
                        break
                name = post["subject"]
                if kt == 0:

                    if "phút trước" in post["date"] or "giờ trước" in post["date"] or "giây trước" in post["date"]:
                        if "man"in name or"Man"in name or"MAn"in name or"MAN"in name or"màn"in name or"Màn"in name or"MÀn"in name or"MÀN" in name:
                            if "24"in name or "27"in name or "30" in name or "32" in name or "19" in name:
                                link +=r"/"+ str(post["list_id"])+".htm"
                                list_old.append(name)
                                cost = post["price_string"]
                                payload = {
                                    "content":f"<@923583677357756487>\n {name} \n Tiền:{cost}\n{link}"
                                }
                                requests.post("https://discord.com/api/webhooks/1322600184307253288/AHDvrNEwmWVtW7z52ejlQOBs7sQ6Y0OsmDSLMzYq5Nv5IBNDwbtcChCyzCtbmh_szw3Q",data=payload)
                                print(list_old)
                                print(link)
        if i == 10:
            payload = {
                "content":f"Vẫn đang chạy và đã chạy được {str(vong)}"
            }
            header ={
                "Authorization":"MTI1MDQ0Nzc3MDMyNjkyNTQwMw.GEbIwT.joHb44-kLjWGKjLrZKzNulwYDy7z1EYD8QGao0"
            }
            requests.post("https://discord.com/api/webhooks/1322600184307253288/AHDvrNEwmWVtW7z52ejlQOBs7sQ6Y0OsmDSLMzYq5Nv5IBNDwbtcChCyzCtbmh_szw3Q",data=payload)
            i = 0

        time.sleep(10)
    except:
        payload = {
    	    "content":f"Vẫn đang bị lỗi và đang cố gắp khôi phục!"
    	}
        header ={
            "Authorization":"MTI1MDQ0Nzc3MDMyNjkyNTQwMw.GEbIwT.joHb44-kLjWGKjLrZKzNulwYDy7z1EYD8QGao0"
        }
        requests.post("https://discord.com/api/webhooks/1322600184307253288/AHDvrNEwmWVtW7z52ejlQOBs7sQ6Y0OsmDSLMzYq5Nv5IBNDwbtcChCyzCtbmh_szw3Q",data=payload)
