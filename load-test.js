import http from 'k6/http';
import { check } from 'k6';

export const options = {
  stages: [
    { duration: '10s', target: 10 },
    { duration: '20s', target: 10 },
    { duration: '10s', target: 0 },
  ],
};

export default function () {
  let res = http.get('http://host.docker.internal:8000/');
  check(res, { 'status was 200': (r) => r.status === 200 });
}