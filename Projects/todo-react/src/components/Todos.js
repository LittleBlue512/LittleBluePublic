import React from 'react';
import PropTypes from 'prop-types';
import TodoItem from './TodoItem';

class Todos extends React.Component {
    render() {
        return this.props.todos.map((todo) => (
            <TodoItem key={todo.id} todo={todo} markCompleted={this.props.markCompleted} delTodo={this.props.delTodo} />
        ))
    }
}

Todos.protoTypes = {
    todos: PropTypes.array.isRequired
}

export default Todos;
