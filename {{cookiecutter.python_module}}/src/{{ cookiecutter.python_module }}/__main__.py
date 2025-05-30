from ngapp.cli.serve_standalone import main as startup

def main():
    startup(app_module="{{ cookiecutter.python_module }}.appconfig")

if __name__ == "__main__":
    main()
