importScripts('https://www.gstatic.com/firebasejs/8.10.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/8.10.0/firebase-messaging.js');

const firebaseApp = firebase.initializeApp({
  apiKey: "AIzaSyBJvSZlEjXMhz4LWoRi1F17kN6n7LKvHyM",
  authDomain: "rock-sublime-252011.firebaseapp.com",
  databaseURL: 'https://project-id.firebaseio.com',
  projectId: "rock-sublime-252011",
  storageBucket: "rock-sublime-252011.appspot.com",
  messagingSenderId: "68029484166",
  appId: "1:68029484166:web:2002ba7ad6d9bba88a9507",
});

const messaging = firebase.messaging();
messaging.onBackgroundMessage((payload) => {
  console.log('[firebase-messaging-sw.js] Received background message ', payload);
  // Customize notification here
  const notificationTitle = 'Background Message Title';
  const notificationOptions = {
    body: 'Background Message body.',
    icon: '/firebase-logo.png'
  };

  self.registration.showNotification(notificationTitle,
    notificationOptions);
});