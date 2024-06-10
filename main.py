from src.manager import ETLManager

if __name__ == "__main__":
    etl_process = ETLManager()  # Default category is GIDA
    etl_process.run_etl()  # 200 products will be extracted
    #etl_process.analyze()  # Analyze the data

    # etl_process.run_etl(total_products=100)  # 100 products will be extracted

    # etl_process_yüzkremi = ETLManager(category="YUZKREMI")  # Category is Yüz Kremi
    # etl_process_yüzkremi.run_etl(total_products=50)  # 50 products will be extracted
