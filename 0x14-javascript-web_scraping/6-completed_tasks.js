#!/usr/bin/node

const request = require('request');
const fs = require('fs');

/** a script that computes the number of tasks completed by user id.**/

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  try {
    const done = {};
    const todos = JSON.parse(body);

    todos.forEach(task => {
      if (task.completed == true) {
        const userId = task.userId;
        if (done[userId]) {
          done[userId]++;
        } else {
          done[userId] = 1;
        }
      }
    });
    console.log(done);
  } catch (err) {
    console.log(err);
  }
});
