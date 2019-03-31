import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
//import App from './App';
import * as serviceWorker from './serviceWorker';


//ReactDOM.render(<App />, document.getElementById('root'));

class CleanBtn extends React.Component {
    handleClick = () => {
        this.props.cleanItm();
    }
    render() {
        if (this.props.left > 0) {
            return <div className='todo-app__clean'>
                <button onClick={this.handleClick}>clean</button>
            </div>
        }
        else {
            return <div className='todo-app__clean'></div>
        }

    }
}
class ViewBtn extends React.Component {
    render() {
        return <ul className='todo-app__view-buttons'>
            <button id="All">All</button>
            <button id="Active">Active</button>
            <button id="Completed">Completed</button>
        </ul>
    }
}
class Total extends React.Component {
    render() {
        return <div className='todo-app__total'>{this.props.left} left</div>;
    }
}
class Checkbox extends React.Component {
    constructor(props) {
        super(props)
        this.state = { checked: this.props.item[1] }
    }
    hadleClick = () => {
        this.setState((state) => ({ checked: !state.checked }));
        this.props.switchState(this.props.itemName)
    }
    render() {
        return <div className='todo-app__checkbox'>
            <input id={`${this.props.index}`} type="checkbox" defaultChecked={this.state.checked} onClick={this.hadleClick} />
            <label htmlFor={`${this.props.index}`} />
        </div>;
    }
}
class Xbtn extends React.Component {
    handleClick = () => {
        this.props.removeItem(this.props.itemName);
    }
    render() {
        return <img className='todo-app__item-x' src='./img/x.png' alt="x" onClick={this.handleClick} />;
    }
}
function listObject(item, index, fn, x) {
    let checkbox = <Checkbox itemName={item[0]} index={index} item={item} switchState={fn} />
    let h1Obj = <h1 className='todo-app__item-detail'>{item[0]}</h1>;
    let img = <Xbtn itemName={item[0]} removeItem={x} />;
    return <li key={item} className='todo-app__item'>{checkbox}{h1Obj}{img}</li>;
}
class TodoAppList extends React.Component {

    render() {
        return <ul className='todo-app__list' id='todo-list'>{this.props.itemList.map((item, index) => listObject(item, index, this.props.switchState, this.props.removeItem))
        }</ul>;
    }
}
class Input extends React.Component {
    handleKey = (event) => {
        if (event.keyCode === 13 && event.target.value !== '') {
            //const newitem = CreateNewTodo(event.target.value)
            const newitem = [
                event.target.value, false
            ];
            this.props.addItem(newitem);
            //appendlist.appendChild(newitem)
            event.target.value = ''
        }
    }
    render() {
        return <input className='todo-app__input' id='todo-input' placeholder='What do you need to bring?' onKeyUp={this.handleKey} />;
    }
}
class Main extends React.Component {
    render() {
        return <section className='todo-app__main'>
            <Input addItem={this.props.addItem} />
            <TodoAppList itemList={this.props.itemList} switchState={this.props.switchState} removeItem={this.props.removeItem} />
        </section>;
    }
}
class Header extends React.Component {
    render() {
        return <span className='todo-app__title'>tobrings</span>;
    }
}
class Footer extends React.Component {
    render() {
        return <footer id="todo-footer" className="todo-app__footer">
            <Total left={this.props.left} />
            <ViewBtn />
            <CleanBtn left={this.props.left} cleanItm={this.props.cleanItm} />
        </footer>

    }
}
class TodoAppRoot extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            "itemList": [
                ["Sunglasses", false],
                ["Baseball cap", false],
                ["Cup", false],
                ["Mouse", false],
                ["Majian", false],
                ["LiangGongSpringDay", false]
            ]
        }
        fetch('http://localhost:5000/list',{body : JSON.stringify(this.state["itemList"]),method : 'POST',mode: 'cors' })
        .then(resp => resp.json())
        .then(data => {console.log(data)})
    }
    updateTable = ()=>{
        console.log("update");
        fetch('http://localhost:5000/look',{body : "123",method : 'POST',mode: 'cors' })
        .then(resp => resp.json())
        .then(data => {console.log(data)})        
    }
    componentDidMount() {
        setInterval(() => this.updateTable(),1000);
    }
    removeItem = (itemName) => {
        let List = this.state["itemList"];
        //List[itemName][1] = !List[itemName][1];
        let ind = List.findIndex((item) => item[0] === itemName);
        List.splice(ind, 1);
        this.setState((state) => ({
            "itemList": List
        }));
        fetch('http://localhost:5000/list',{body : JSON.stringify(this.state["itemList"]),method : 'POST',mode: 'cors' })
        .then(resp => resp.json())
        .then(data => {console.log(data)})
    }
    switchState = (itemName) => {
        let List = this.state["itemList"];
        //List[itemName][1] = !List[itemName][1];
        let ind = List.findIndex((item) => item[0] === itemName);
        List[ind][1] = !List[ind][1];
        this.setState((state) => ({
            "itemList": List
        }));
        fetch('http://localhost:5000/list',{body : JSON.stringify(this.state["itemList"]),method : 'POST',mode: 'cors' })
        .then(resp => resp.json())
        .then(data => {console.log(data)})
    }
    addItem = (newitem) => {
        let List = this.state["itemList"];
        List.push(newitem);
        this.setState((state) => ({
            "itemList": List
        }));
    }
    cleanItm = () => {
        let List = this.state["itemList"];
        let newList = List.filter(item => item[1] === false);
        this.setState(
            () => ({ "itemList": newList })
        );
        fetch('http://localhost:5000/list',{body : JSON.stringify(this.state["itemList"]),method : 'POST',mode: 'cors' })
        .then(resp => resp.json())
        .then(data => {console.log(data)})
    }
    render() {
        return <>
            <Header />
            <Main itemList={this.state["itemList"]} switchState={this.switchState} removeItem={this.removeItem} addItem={this.addItem} />
            {/* <Footer left={this.state["itemList"].reduce((acc, item) => acc + (item[1] === false), 0)} cleanItm={this.cleanItm} /> */}
            <Footer left={this.state["itemList"].filter((item)=> item[1] === false).length} cleanItm={this.cleanItm} /> 
        </>
    }
}
ReactDOM.render(<TodoAppRoot />, document.getElementById('root'));
// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
