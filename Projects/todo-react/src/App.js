import React from 'react';
import Header from './components/layout/Header';
import Todos from './components/Todos';
import AddTodo from './components/AddTodo';
import uuid from 'uuid';

import './App.css';

class App extends React.Component {
  constructor() {
    super();
    this.state = {
      todos: [
        {
          id: uuid.v4(),
          title: "Practice Calculus",
          completed: false
        },
        {
          id: uuid.v4(),
          title: "Java Project",
          completed: false
        },
        {
          id: uuid.v4(),
          title: "React Project",
          completed: false
        }
      ]
    }
  }

  markCompleted = (id) => {
    this.setState({
      todos: this.state.todos.map((todo) => {
        if (todo.id === id) {
          todo.completed = !todo.completed;
        }
        return todo
      })
    });
  }

  delTodo = (id) => {
    this.setState({
      todos: [...this.state.todos.filter(todo => todo.id !== id)]
    });
  }

  addTodo = (title) => {
    const newTodo = {
      id: uuid.v4(),
      title: title,
      completed: false
    }
    this.setState({ todos: [...this.state.todos, newTodo] })
  }

  render() {
    return (
      <div className="App">
        <div className="container">
          <Header />
          <AddTodo addTodo={this.addTodo} />
          <Todos todos={this.state.todos} markCompleted={this.markCompleted} delTodo={this.delTodo} />
        </div>
      </div>
    );
  }
}

export default App;
