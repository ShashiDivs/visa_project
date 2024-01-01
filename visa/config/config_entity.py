from collections import namedtuple

DataIngestionConfig:namedtuple("DataIngestionConfig",
                               ["dataset_downlaod_url","raw_data_dir",
                                "ingested_dir","ingetsed_train_dir","ingetsed_test_dir"])


DataValidationConfig:namedtuple("DataValidationConfig",["schema_file_dir"])