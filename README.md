# Trendyol Scraping Project

This project is designed to extract product data from Trendyol, transform it, and load it into a MySQL database. The project is structured using an ETL (Extract, Transform, Load) pipeline, with the ability to handle different product categories dynamically.

## Table of Contents
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [License](#license)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
docker build -t trendyol_scrapy .
docker run --name trendyol_container trendyol_scrapy
```
If you want to run container with images in your host machine (Also you need to change the file_path in analyze.py file)
```bash
docker run -v /host/path/to/images:/path/in/container -it your_docker_image
```



## Usage

```python
from src.manager import ETLManager
etl_process = ETLManager()  # Default category is GIDA
etl_process.run_etl()  # 200 products will be extracted
#etl_process.analyze()  # Analyze the data

# etl_process.run_etl(total_products=100)  # 100 products will be extracted

# etl_process_yüzkremi = ETLManager(category="YUZKREMI")  # Category is Yüz Kremi
# etl_process_yüzkremi.run_etl(total_products=50)  # 50 products will be extracted
```

## Configuration
The project uses a configuration dictionary to manage different categories. This configuration includes the URL, base API URL, and the category name.
### Example Configuration
```
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

```



## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
