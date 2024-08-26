from flask import Flask, render_template, request
import pickle
import numpy as np

model = pickle.load(open('Model.pkl', 'rb'))
book_names = pickle.load(open('Book_Names.pkl', 'rb'))
book_pivot = pickle.load(open('Book_Pivot.pkl', 'rb'))
final_rating = pickle.load(open('Final_Rating.pkl', 'rb'))

app = Flask(__name__)


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books', methods=['post'])
def recommend_book(book_name):
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6 )

    for i in range(len(suggestion)):
            books = book_pivot.index[suggestion[i]]
            for j in books:
                if j == book_name:
                    print(f"You searched '{book_name}'\n")
                    print("The suggestion books are: \n")
                else:
                    print(j)


book_name = "Harry Potter and the Chamber of Secrets (Book 2)"
recommend_book(book_name)

if __name__ == '__main__':
    app.run(debug=True)
