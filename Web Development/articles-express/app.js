const bodyParser = require('body-parser');
const express = require('express');
const path = require('path');
const mongoose = require('mongoose');

const Article = require('./models/article');

const app = express();

const port = 5000;

// Connect to database
mongoose.connect('mongodb://localhost/articles', { useNewUrlParser: true, useUnifiedTopology: true });
const db = mongoose.connection;

// Start server
app.listen(port, () => console.log(`Server started on port ${port}...`));

// Load view engine
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

// Setup public folder
app.use(express.static(path.join(__dirname, 'public')));

// Setup body-parser
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// Home route
app.get('/', (req, res) => {
    Article.find((err, articles) => {
        if (err)
            console.log(err);
        else {
            res.render('index', {
                title: 'Home',
                articles: articles
            });
        }
    });
});

// Add article form
app.get('/articles/add', (req, res) => {
    res.render('add_article', {
        title: 'Add Article'
    });
});

// Add article to database
app.post('/articles/add', (req, res) => {
    let { title, author, content } = req.body;
    let newArticle = new Article({ title, author, content });
    newArticle.save((err) => {
        if (err)
            console.log(err);
        else
            res.redirect('/');
    });
});

// Show the article
app.get('/articles/:id', (req, res) => {
    Article.findById(req.params.id, (err, article) => {
        if (err)
            console.log(err);
        else {
            res.render('article', {
                article: article
            });
        }
    });
});

// Edit the article
app.get('/articles/edit/:id', (req, res) => {
    Article.findById(req.params.id, (err, article) => {
        if (err)
            console.log(err)
        else {
            res.render('edit_article', {
                title: 'Edit Article',
                article: article
            });
        }
    });
});

// Update editted article
app.post('/articles/edit/:id', (req, res) => {
    let query = { _id: req.params.id };
    let { title, author, content } = req.body;
    Article.updateOne(query, {
        title: title,
        author: author,
        content: content
    }, (err) => {
        if (err)
            console.log(err)
        else {
            res.redirect('/');
        }
    });
});

// Delete article
app.delete('/articles/:id', (req, res) => {
    let query = { _id: req.params.id };
    Article.deleteOne(query, (err) => {
        if (err)
            console.log(err);
        else
            res.send('success');
    });
});