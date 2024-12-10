from ir_ocr import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)  # You can set debug to False in production
