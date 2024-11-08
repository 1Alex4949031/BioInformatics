from prefect import flow

@flow
def hello_world():
    print("Hello, World!")

hello_world()