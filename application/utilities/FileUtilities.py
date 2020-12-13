
class FileUtilities:
    @staticmethod
    def load_credentials_db (file_):
        credentials = {}
        try:
            with open(file_, 'r' ) as cred_db :
                credentials = dict (x.rstrip().split("=") for x in cred_db.readlines())
        except FileNotFoundError as error_fn:
            print (f'unable to load file {file_} error {error_fn}')
        finally:
            return credentials
