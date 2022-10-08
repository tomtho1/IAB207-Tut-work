from travel import create_app

if __name__ == '__main__':
    new_app = create_app()
    new_app.run(debug=True) #if app crashes it will be rerun with errors presented by the interpreter 
    