const ejs = require('ejs');
const path = require('path');
const mysql = require('mysql');
const bcrypt = require('bcrypt');
const express = require('express');
const session = require('express-session');
const MySQLStore = require('express-mysql-session')(session);

const {
    PORT = 5000,
    SALT_ROUNDS = 10,

    SESS_NAME = 'sid',
    SESS_LIFETIME = 1000 * 60 * 60
} = process.env;

const database_option = {
    host: 'localhost',
    user: 'root',
    password: '0000',
    database: 'session_test'
};

const sessionStore_option = {
    host: 'localhost',
    port: '3306',
    user: 'root',
    password: '0000',
    database: 'session_test'
};

const app = express();
const sessionStore = new MySQLStore(sessionStore_option);
const DBcon = mysql.createConnection(database_option);

DBcon.connect();

app.use(session({
    secret: 'unknownenemy',
    store: sessionStore,
    resave: false,
    saveUninitialized: false,
    name: SESS_NAME,
    cookie: {
        maxAge: SESS_LIFETIME
    }
}));

app.listen(PORT, () => console.log(`Server started on port ${PORT}...`)) // DEV

app.use(express.urlencoded({ extended: false }));

// Take user to Welcomepage if they are not logged-in
function redirectToWelcome(req, res, next) {
    if (!req.session.userId) {
        return res.redirect('/');
    }
    next();
}

// Take user to Homepage if they are logged-in
function redirectToHome(req, res, next) {
    if (req.session.userId) {
        return res.redirect('/home');
    }
    next();
}

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'public/welcome.html'));
});

app.get('/home', redirectToWelcome, (req, res) => {
    const { name } = req.session;
    ejs.renderFile('./public/home.html', { name: name }, (err, str) => {
        if (err) throw err;
        res.send(str);
    });
});

app.get('/login', redirectToHome, (req, res) => {
    res.sendFile(path.join(__dirname, 'public/login.html'));
});

app.get('/register', redirectToHome, (req, res) => {
    res.sendFile(path.join(__dirname, 'public/register.html'));
});

app.post('/login', redirectToHome, (req, res) => {
    const { email, password } = req.body;
    if (!email || !password) {
        // Invalid
        console.log("Invalid login: Not fill in all fields") // DEV
        res.sendfile(path.join(__dirname, 'public/login.html'))
    } else {
        // Valid
        // Check if user exists in DB
        let sql = 'SELECT * FROM users WHERE email = ?';
        DBcon.query(sql, [email], (err, result) => {
            if (err) throw err;
            if (result[0]) {
                console.log('Valid login: Email found'); // DEV
                // User exists
                let { userId, name, email } = result[0];
                let passwordHash = result[0].password;
                // Check if password is correct
                bcrypt.compare(password, passwordHash, (err, result) => {
                    if (err) throw err;
                    if (result) {
                        // Correct
                        console.log('User login: Password matched'); // DEV
                        // Log user in
                        req.session.userId = userId;
                        req.session.name = name;
                        // Take user to Homepage
                        res.redirect('/home');
                    } else {
                        // Wrong
                        console.log('Invalid login: Password is wrong'); // DEV
                        res.redirect('/login');
                    }
                });
            } else {
                // User not exists
                console.log('Invalid login: Email not found'); // DEV
                res.redirect('/login');
            }
        });
    }
});

app.post('/logout', redirectToWelcome, (req, res) => {
    req.session.destroy((err) => {
        if (err) throw err;
        console.log('User logout: Session destroyed'); // DEV
        res.redirect('/');
    });
});

app.post('/register', redirectToHome, (req, res) => {
    const { name, email, password } = req.body;
    if (!name || !email || !password) {
        // Invalid
        console.log("Invalid register: Not fill in all fields") // DEV
        res.sendFile(path.join(__dirname, 'public/register.html'))
    } else {
        // Valid
        // Check if user already exists in DB
        let sql = 'SELECT * FROM users WHERE email = ?';
        DBcon.query(sql, [email], (err, result) => {
            if (err) throw err;
            // Check if there are any data in result
            if (result[0]) {
                // User already exists in DB
                console.log("Invalid register: User already exists in database") // DEV
                res.sendFile(path.join(__dirname, 'public/register.html'));
            } else {
                // Add user to DB
                bcrypt.hash(password, SALT_ROUNDS, (err, result) => {
                    if (err) throw err;
                    let sql = 'INSERT INTO users (name, email, password) VALUES (?, ?, ?)'
                    DBcon.query(sql, [name, email, result], (err, result) => {
                        if (err) throw err;
                        console.log('Valid register: log user in'); // DEV
                        // Log user in
                        req.session.userId = result.insertId;
                        req.session.name = name;
                        // Take user to Homepage
                        res.redirect('/home');
                    });
                });
            }
        });
    }
});