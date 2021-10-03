import { Injectable } from '@angular/core';
import { webSocket } from 'rxjs/webSocket';
import { retry } from 'rxjs/operators';
import { ChallengeResult } from './scoreboard/scoreboard.component';
import { BehaviorSubject } from 'rxjs';

const BACKEND_URL = "ws://localhost:8765";

@Injectable({
  providedIn: 'root'
})
export class ScoreboardWebsocketService {
  constructor() {
  }

  private RECEIVED_DATA = new BehaviorSubject<ChallengeResult[]>([]);
  data$ = this.RECEIVED_DATA.asObservable()

  connect() {
    const subject = webSocket(BACKEND_URL);
    subject.pipe(
      retry()
    ).subscribe({
      next: msg => this.receiveData(msg as ChallengeResult), // Called whenever there is a message from the server.
      error: err => console.log(err), // Called if at any point WebSocket API signals some kind of error.
    });
  }

  private receiveData(msg: ChallengeResult): void {
    console.log("Got data: " + JSON.stringify(msg))
    const previous = this.RECEIVED_DATA.getValue();
    const next = previous.concat([msg]);
    this.RECEIVED_DATA.next(next)
  }
}
