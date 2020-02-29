from modelarts.session import Session

def div2k_dowloader():
    session = Session()
    bucket_path="/cv-course-public/coding-3/high\ resolution\ images/DIV2K_train_HR.zip"
    session.download_data(bucket_path=bucket_path, path="./data/DIV2K_train_HR.zip")