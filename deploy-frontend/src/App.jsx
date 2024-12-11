import React, { useEffect, useState } from "react"
import axios from "axios";
import './App.css'


export default function App() {
  const [items, setItems] = useState([]);
  const baseUrl = 'http://87.228.36.65/api';

  const fetchItems = () => {
    axios.get(`${baseUrl}/items`)
    .then(response => {
      const responseItems = response.data;
      setItems(responseItems);
    })
    .catch(errors => {
      console.log(errors);
    });
  };

  useEffect(() => {
    fetchItems();
  }, []);

  return (
    <div className="items">
      {items.map(item => (
        <div key={item.id} className="item">
          <img width={150} src={item.url} alt="" />
          <p>{item.name}</p>
        </div>
      ))}
    </div>
  );
};
