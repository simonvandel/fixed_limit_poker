import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';
import { ScoreboardComponent } from './scoreboard/scoreboard.component';
import { MatTableModule } from '@angular/material/table';
import { CommonModule } from '@angular/common';
import { CdkTableModule } from '@angular/cdk/table';
import { ScoreboardWebsocketService } from './scoreboard-websocket.service';

@NgModule({
  declarations: [
    ScoreboardComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    NoopAnimationsModule,
    MatTableModule,
    CommonModule,
    CdkTableModule,
  ],
  providers: [ScoreboardWebsocketService],
  entryComponents: [ScoreboardComponent],
  bootstrap: [ScoreboardComponent]
})
export class AppModule { }
