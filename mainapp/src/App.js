import './App.css';
import Header from './header';
import Sidebar from './Sidebar';
import Content from './Content';
import Footer from './Footer';
function App() {
  return (
    <div className="App">
      <Header />
      <div className="main">
        <Sidebar />
        <Content />
      </div>
      <Footer />
    </div>
  );
}

export default App;