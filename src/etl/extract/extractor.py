#!/usr/bin/env python3
import re
import requests
import pandas as pd
from typing import Optional
from src.logger import CustomLogger
from .extract_helper import ExtractHelper
from config import category_config_parser


class Extractor:
    def __init__(self, category: str):
        self.__url = category_config_parser[category]["URL"]
        self.__base_api_url = category_config_parser[category]["BASE_API_URL"]
        self.__extract_helper = ExtractHelper(category_config_parser[category]["NAME"])

        self.__logger = CustomLogger(logger_name="Trendyol Scraper").logger

    def __get_page_content(self) -> str:
        _headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
            "accept-language": "en-US,en;q=0.8",
            "cache-control": "no-cache",
            "pragma": "no-cache",
            "priority": "u=0, i",
            "sec-ch-ua": '"Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "sec-gpc": "1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        }
        response = requests.get(self.__url, headers=_headers)
        response.raise_for_status()
        return response.text

    def __extract_offset(self, html_content: str) -> Optional[str]:
        offset_match = re.search(r'"offset":(\d+)', html_content)
        if offset_match:
            return offset_match.group(1)
        return None

    def __get_more_products(self, pi: int, offset: str) -> dict:
        headers = {
            "accept": "application/json, text/plain, */*",
            "accept-language": "en-US,en;q=0.8",
            "cache-control": "no-cache",
            "origin": "https://www.trendyol.com",
            "pragma": "no-cache",
            "priority": "u=1, i",
            "sec-ch-ua": '"Brave";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "sec-gpc": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        }
        api_url = f"{self.__base_api_url}?pi={pi}&culture=tr-TR&userGenderId=1&pId=0&isLegalRequirementConfirmed=false&searchStrategyType=DEFAULT&productStampType=TypeA&scoringAlgorithmId=2&fixSlotProductAdsIncluded=true&searchAbDecider=&location=null&offset={offset}&channelId=1"
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        return response.json()

    def extract(self, total_products: int = 100) -> pd.DataFrame:
        self.__logger.info("Extracting products from Trendyol...")
        html_content = self.__get_page_content()
        products = self.__extract_helper.extract_products_from_html(html_content)
        offset = self.__extract_offset(html_content)
        pi = 2

        while len(products) < total_products:
            if offset is None:
                break
            json_data = self.__get_more_products(pi, offset)
            new_products = self.__extract_helper.extract_products_from_json(json_data)
            products.extend(new_products)
            offset = json_data["result"].get("offset")
            pi += 1
        self.__logger.info(f"Total products extracted: {len(products[:total_products])}")
        return pd.DataFrame(products[:total_products])