const mongoose = require('mongoose');

// Article schema
const articleSchema = mongoose.Schema({
    title: {
        type: String,
        require: true
    },
    author: {
        type: String,
        require: true
    },
    content: {
        type: String,
        require: true
    }
});

const Article = module.exports = mongoose.model('Article', articleSchema);