import React from 'react';
import PropTypes from 'prop-types';

class TodoItem extends React.Component {
    getStyle() {
        return {
            background: '#f4f4f4',
            padding: '10px',
            borderBottom: '1px #ccc dotted',
            textDecoration: this.props.todo.completed ? 'line-through' : 'none'
        }
    }

    render() {
        const { id, title } = this.props.todo;
        return (
            <div style={this.getStyle()}>
                <input type="checkBox" onChange={this.props.markCompleted.bind(this, id)} /> {' '}
                {title}
                <button style={btnStyle} onClick={this.props.delTodo.bind(this, id)}>X</button>
            </div>
        );
    }
}

TodoItem.propTypes = {
    todo: PropTypes.object.isRequired
}

const btnStyle = {
    background: "#ff0000",
    color: "#fff",
    border: "none",
    padding: "5px 10px",
    borderRadius: "50%",
    cursor: "pointer",
    float: "right"
}

export default TodoItem;