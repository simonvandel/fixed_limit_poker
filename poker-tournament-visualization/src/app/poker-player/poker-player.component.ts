import { Component, Input, OnInit } from '@angular/core';
import { Player } from '../poker-game/poker-game.service';

@Component({
  selector: 'app-poker-player',
  templateUrl: './poker-player.component.html',
  styleUrls: ['./poker-player.component.css']
})
export class PokerPlayerComponent implements OnInit {
  @Input() player!: Player;

  constructor() { }

  ngOnInit(): void {
  }

}
