def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

def check_alien_bottom(ai_settings, screen, stats, sb, ship, aliens, bullets):
    # ...existing code...
    if len(aliens) == 0:
        # Destroy existing bullets and create new fleet
        bullets.empty()
        ai_settings.increase_speed()
        create_fleet(ai_settings, screen, ship, aliens)
        stats.level += 1
        sb.prep_level()
    check_high_score(stats, sb)  # Add this line
