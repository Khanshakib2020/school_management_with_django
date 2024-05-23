// import Navbar from '../components/Navbar';
// import Sidebar from '../components/Sidebar';

import Navbar from "./components/navbar";
import Sidebar from "./components/sidebar";

export default function Home() {
  return (
    <div>
      <Navbar />
      <main>
        <h1>Home Page</h1>
      </main>
      <Sidebar />
    </div>
  );
}
