#!/usr/bin/env python3
import configparser

category_config_parser = configparser.ConfigParser()

url = "https://www.trendyol.com"
base_api_url = (
    "https://public.trendyol.com/discovery-web-searchgw-service/v2/api/infinite-scroll"
)

category_config_parser["GIDA"] = {
    "NAME": "Gıda ve İçecek",
    "URL": f"{url}/gida-ve-icecek-x-c103946",
    "BASE_API_URL": f"{base_api_url}/gida-ve-icecek-x-c103946",
}


category_config_parser["BEBEK"] = {
    "NAME": "Bebek Bakım",
    "URL": f"{url}/bebek-bakim-ve-kozmetik-x-c105559",
    "BASE_API_URL": f"{base_api_url}/bebek-bakim-ve-kozmetik-x-c105559",
}

category_config_parser["YUZKREMI"] = {
    "NAME": "Yüz Kremi",
    "URL": f"{url}/yuz-kremi-x-c1122",
    "BASE_API_URL": f"{base_api_url}/yuz-kremi-x-c1122",
}
