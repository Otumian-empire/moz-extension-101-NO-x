# read urls in sites.txt and convert it to
#  "*://*.site-name.com/*"


def format_url(url):
    site = ""

    if "#" in url:
        url = url.split("#")[0]
    elif "?" in url:
        url = url.split("?")[0]

    url = url.strip("/")

    if "www" in url:
        site = url.split("www.")[1]
    elif url.startswith("http"):
        site = url.split("//")[1]

    return f"*://*.{site}/*"


try:
    matches_list = []

    with open("sites.txt", "r") as ptr:
        for url in ptr.readlines():
            if "join" in url or "track" in url:
                continue

            if "http" in url:
                matches_list.append(format_url(url.strip("\n")))

        # In match_list.txt, convert ' to " for json
        with open("match_list.txt", "w+") as fptr:
            print(matches_list, file=fptr)

except Exception as e:
    print(str(e))
