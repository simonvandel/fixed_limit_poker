import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { PokerGameComponent } from './poker-game.component';
import { PokerGameService } from './poker-game.service';
import { PokerTableComponent } from '../poker-table/poker-table.component';
import { PokerPlayerComponent } from '../poker-player/poker-player.component';
import { MatSliderModule } from '@angular/material/slider';
import { FormsModule } from '@angular/forms';
import { PokerActionComponent } from '../poker-action/poker-action.component';
import { CardGroupComponent } from '../card-group/card-group.component';
import { MatGridListModule } from '@angular/material/grid-list';
import { MatIconModule } from '@angular/material/icon';
import { MatButtonModule } from '@angular/material/button';
import { MatButtonToggleModule } from '@angular/material/button-toggle';

@NgModule({
  declarations: [
    PokerGameComponent,
    PokerTableComponent,
    PokerPlayerComponent,
    PokerActionComponent,
    CardGroupComponent,
  ],
  imports: [
    CommonModule,
    MatSliderModule,
    MatGridListModule,
    FormsModule,
    MatIconModule,
    MatButtonModule,
    MatButtonToggleModule,
  ],
  exports: [PokerGameComponent],
  providers: [PokerGameService],
})
export class PokerGameModule {}
