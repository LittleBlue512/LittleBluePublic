class Book {
    constructor(title, author, number) {
        this.title = title;
        this.author = author;
        this.number = number;
    }
}

class UI {
    static displayBook() {
        const StoredBooks = Store.getBooks();

        const books = StoredBooks;

        books.forEach(function (book) {
            UI.addBookToList(book);
        })
    }

    static addBookToList(book) {
        const list = document.querySelector('#book-list');
        const row = document.createElement('tr')
        row.innerHTML = '<td>' + book.title + '</td>'
            + '<td>' + book.author + '</td>'
            + '<td>' + book.number + '</td>'
            + '<td><a href="#" class="btn btn-danger btn-sm delete">X</a></td>';
        list.appendChild(row);
    }

    static removeBook(e) {
        if (e.classList.contains('delete')) {
            e.parentElement.parentElement.remove();
        }
    }

    static showAlert(message, _className) {
        const div = document.createElement('div');
        div.className = 'alert alert-' + _className;
        div.appendChild(document.createTextNode(message));
        const container = document.querySelector('.container');
        const form = document.querySelector('#book-form');
        container.insertBefore(div, form);
        setTimeout(function () {
            document.querySelector('.alert').remove();
        }, 3000);
    }

    static clearFields() {
        document.querySelector('#title').value = '';
        document.querySelector('#author').value = '';
        document.querySelector('#number').value = '';
    }
}

class Store {
    static getBooks() {
        let books;
        if (localStorage.getItem('books') == null) {
            books = [];
        } else {
            books = JSON.parse(localStorage.getItem('books'));
        }
        return books;
    }

    static addBook(book) {
        const books = Store.getBooks();
        books.push(book);
        localStorage.setItem('books', JSON.stringify(books));
    }

    static removeBook(number) {
        const books = Store.getBooks();
        books.forEach(function (book, index) {
            if (book.number === number) {
                books.splice(index, 1);
            }
        });
        localStorage.setItem('books', JSON.stringify(books));
    }

    static containsBook(number) {
        const books = Store.getBooks('books');
        var found = false;
        books.forEach(function(book) {
            console.log(book.number, number);
            if(book.number === number) {
                found = true;
            }
        });
        return found;
    }
}

document.addEventListener('DOMContentLoaded', UI.displayBook());

document.querySelector('#book-form').addEventListener('submit', function (e) {
    const title = document.querySelector('#title').value;
    const author = document.querySelector('#author').value;
    const number = document.querySelector('#number').value;

    if (title == '' || author == '' || number == '') {
        UI.showAlert('Please fill in all fields', 'danger');
    } else if(Store.containsBook(number)) {
        UI.showAlert('Book number ' + number + ' is already added', 'warning');
    } else {
        const book = new Book(title, author, number);

        UI.addBookToList(book);

        Store.addBook(book);

        UI.showAlert('Book Added', 'success');

        UI.clearFields();
    }
})

document.querySelector('#book-list').addEventListener('click', function (e) {
    UI.removeBook(e.target);
    Store.removeBook(e.target.parentElement.previousElementSibling.textContent);
    UI.showAlert('Book removed', 'success');
});