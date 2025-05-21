from webapp_client.cli.serve_standalone import main as startup

def main():
    startup(app_module="{{ cookiecutter.module_name }}.appconfig")

if __name__ == "__main__":
    main()
